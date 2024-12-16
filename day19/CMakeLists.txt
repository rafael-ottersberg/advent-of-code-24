add_library( day19 day19.cpp)

target_include_directories(day19 PRIVATE ${CMAKE_CURRENT_LIST_DIR})

target_link_libraries( day19 TBB::tbb )