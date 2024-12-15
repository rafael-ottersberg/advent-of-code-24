add_library( day0 day0.cpp)

target_include_directories(day0 PRIVATE ${CMAKE_CURRENT_LIST_DIR})

target_link_libraries( day0 TBB::tbb )